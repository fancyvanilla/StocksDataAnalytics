import java.io.IOException;

import javax.naming.Context;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class AvgPerDay {

    public static class AvgPerDayMapper extends Mapper<LongWritable, Text, Text, Text> {

        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            
            if (key.get() == 0) {
                return; // Skip processing the header line
            }
            // Split the CSV line into columns
            String[] columns = value.toString().split(",");
            
            if (columns.length < 11)
            {
                return;
            }
            String stockPrice = columns[5]; // 'PRICE' column index is 5
            try{
             Double intValue = Double.parseDouble(stockPrice);
            }
            catch(NumberFormatException e) {
                return;
            }
            String stockDate = columns[0]; // 'DATE' column index is 0
            context.write(new Text(stockDate), new Text(stockPrice));
        }
    }

    public static class AvgPerDayReducer extends Reducer<Text, Text, Text, Text> {

        @Override
        public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            int count = 0;
            for (Text value : values) {
                sum += Double.parseDouble(value.toString());
                count++;
            }
            int avgPerDay = (int) Math.round((double) sum / count);
            context.write(key, new Text(String.valueOf(avgPerDay)));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Average Day Prices Analysis");
        job.setJarByClass(AvgPerDay.class);
        job.setMapperClass(AvgPerDayMapper.class);
        job.setReducerClass(AvgPerDayReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0])); // Input CSV file path
        FileOutputFormat.setOutputPath(job, new Path(args[1])); // Output directory path
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}