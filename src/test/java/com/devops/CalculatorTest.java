package com.devops;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import com.example.Calculator;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    void testAdd() {
        assertEquals(15, calc.add(10,5));
    }

    @Test
    void testSubtract() {
        assertEquals(5, calc.subtract(10,5));
    }

    @Test
    void testMultiply() {
        assertEquals(50, calc.multiply(10,5));
    }

    @Test
    void testDivide() {
        assertEquals(2, calc.divide(10,5));
    }

    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> calc.divide(10,0));
    }

    @Test
    void testNegativeResult() {
        assertEquals(-5, calc.subtract(5,10));
    }
}