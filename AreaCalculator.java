public class AreaCalculator {

    // Method to calculate area of rectangle
    public double calculateArea(double length, double width) {
        return length * width;
    }

    // Method to calculate area of circle
    public double calculateArea(double radius) {
        return Math.PI * radius * radius;
    }

    // Method to calculate area of triangle
    public double calculateArea(double base, double height, String shape) {
        if (shape.equalsIgnoreCase("triangle")) {
            return 0.5 * base * height;
        } else {
            System.out.println("Invalid shape. Cannot calculate area.");
            return -1;
        }
    }

    public static void main(String[] args) {
        AreaCalculator calculator = new AreaCalculator();

        // Calculate area of rectangle
        double rectangleArea = calculator.calculateArea(5, 10);
        System.out.println("Area of rectangle: " + rectangleArea);

        // Calculate area of circle
        double circleArea = calculator.calculateArea(4);
        System.out.println("Area of circle: " + circleArea);

        // Calculate area of triangle
        double triangleArea = calculator.calculateArea(3, 4, "triangle");
        System.out.println("Area of triangle: " + triangleArea);
    }
}
