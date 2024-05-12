// Superclass
class Shape {
    // Method to calculate area (to be overridden by subclasses)
    public double calculateArea() {
        return 0;
    }
}

// Subclass for Rectangle
class Rectangle extends Shape {
    private double length;
    private double width;

    // Constructor
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    // Override calculateArea() method
    @Override
    public double calculateArea() {
        return length * width;
    }
}

// Subclass for Circle
class Circle extends Shape {
    private double radius;

    // Constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    // Override calculateArea() method
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

// Subclass for Triangle
class Triangle extends Shape {
    private double base;
    private double height;

    // Constructor
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    // Override calculateArea() method
    @Override
    public double calculateArea() {
        return 0.5 * base * height;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create objects of different shapes
        Rectangle rectangle = new Rectangle(5, 10);
        Circle circle = new Circle(4);
        Triangle triangle = new Triangle(3, 4);

        // Calculate and print areas
        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        System.out.println("Area of circle: " + circle.calculateArea());
        System.out.println("Area of triangle: " + triangle.calculateArea());
    }
}
