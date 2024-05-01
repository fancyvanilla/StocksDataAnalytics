import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

public class MovingAvg {

    public static class MovingAvgMapper extends Mapper<LongWritable, Text, Text, Text> {
        private int windowSize = 10; 
        private Map<String, List<Double>> priceWindow = new HashMap<>() ;

        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            
            if (key.get() == 0) {
                return; 
            }

            String[] columns = value.toString().split(",");
            
            if (columns.length < 11)
            {
                return;
            }

            String stockPrice = columns[5]; 
            String stockCode=columns[2]; 
            String stockDate = columns[0]; 

            try{
             Double intValue = Double.parseDouble(stockPrice);
            }
            catch(NumberFormatException e) {
                return;
            }
            Double price=Double.parseDouble(stockPrice);

            List<Double> codeWindow = priceWindow.get(stockCode);
            double movingAvg=price;

            if (codeWindow == null) {
            codeWindow = new ArrayList<>();
            }
            codeWindow.add(price);
            if (codeWindow.size() > windowSize) {
              codeWindow.remove(0); // Remove oldest element if window is full
            }
            if (codeWindow.size() == windowSize) {
                movingAvg = codeWindow.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
              }
            priceWindow.put(stockCode,codeWindow);
            context.write(new Text(stockCode), new Text(String.format("%.2f", movingAvg)));

        }
    }


    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Moving Average Price");
        job.setJarByClass(MovingAvg.class);
        job.setMapperClass(MovingAvgMapper.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0])); // Input CSV file path
        FileOutputFormat.setOutputPath(job, new Path(args[1])); // Output directory path
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}