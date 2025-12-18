package org.example;

public class Tracer {
    private static boolean trace=false;
    static void trace(String message){
        if(trace)
            System.out.println(message);
    }

    public static void main(String[] args) {
        Tracer.on();
        Tracer.trace( "Start" );
        int i = 2;
        Tracer.off();
        Tracer.trace( "i = " + i );
//  Tracer.trace( "i = %d", i );
        Tracer.on();
        Tracer.trace( "End" );
    }
    static void trace(String format, Object... args){
        if(trace)
            System.out.printf(format, args);
    }

    static void on(){
        trace = true;
    }
    static void off(){
        trace = false;
    }
}
