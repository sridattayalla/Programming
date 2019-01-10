package com.company;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;



public class test {
    static String BOOKING_ID = "656FDS4FD4";
    static String total_cost = "242";
    public static void main(String args[]) {
        try {
            // Construct data
            String apiKey = "apikey=" + "BEEWJxdS9w8-zcLCp1lQCU6Ff980adLChVtGTnHYe5";
            String message = "&message=" + "Booking Successful, Booking Id: 656FDS4FD4, DirectPay:₹ 242";
            System.out.print(message);
            String sender = "&sender=" + "SLTSED";
            String numbers = "&numbers=" + "918688871288";

            // Send data
            HttpURLConnection conn = (HttpURLConnection) new URL("https://api.textlocal.in/send/?").openConnection();
            String data = apiKey + numbers + message + sender;
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Length", Integer.toString(data.length()));
            conn.getOutputStream().write(data.getBytes("UTF-8"));
            final BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            final StringBuffer stringBuffer = new StringBuffer();
            String line;
            while ((line = rd.readLine()) != null) {
                stringBuffer.append(line);
            }
            rd.close();
            System.out.print(stringBuffer.toString());

        } catch (Exception e) {
            System.out.println("Error SMS "+e);

        }
    }
}