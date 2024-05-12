// Java program to illustrate the
// concept of Multilevel inheritance
import java.io.*;
import java.lang.*;
import java.util.*;

class One {
	public void print_geek()
	{
		System.out.println("Geeks");
	}
}

class Two extends One {
	public void print_for() { System.out.println("for"); }
}

class Three extends Two {
	public void print_geek()
	{
		System.out.println("Geeks");
	}
}

// Drived class
class multilevelinheritance{
	public static void main(String[] args)
	{
		Three g = new Three();
		g.print_geek();
		g.print_for();
		g.print_geek();
	}
}
