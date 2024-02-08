import java.util.ArrayList;
import java.util.List;

class Solution {
    public int reverse1(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return (int) number;
    }

    public int reverse2(int x) {
        int sign = x < 0 ? -1 : 1;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == -1 ? -number : number;
        return number;
    }

    public int reverse3(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse4(int x) {
        int sign = (x < 0) ? 1 : 0;
        int y = (x < 0) ? -x : x;
        
        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }
        
        int number = 0;
        int length = digits.size();
        
        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }
        
        number = (sign == 1) ? -number : number;
        return number;
    }

    public int reverse5(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;
        
        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }
        
        int number = 0;
        int length = digits.size();
        
        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }
        
        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse6(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<Integer>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y/10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse7(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse8(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse9(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse10(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();

        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse11(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y /= 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            double power = Math.pow(10, length - i - 1);
            number += digits.get(i) * power;
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse12(int x) {
        int sign = x < 0 ? -1 : 1;
        int y = x < 0 ? -x : x;
        
        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int remainder = y % 10;
            digits.add(remainder);
            y = y / 10;
        }
        
        int number = 0;
        int length = digits.size();
        
        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }
        
        number = sign == -1 ? -number : number;
        return number;
    }

    public int reverse13(int x) {
        int sign = x < 0 ? -1 : 1;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int remainder = y % 10;
            digits.add(remainder);
            y = y/10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == -1 ? -number : number;
        return number;
    }

    public int reverse14(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse15(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;
        
        java.util.ArrayList<Integer> digits = new java.util.ArrayList<>();
        
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = (int) y/10;
        }
        
        int number = 0;
        int length = digits.size();
        
        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }
        
        number = sign == 1 ? -number : number;
        return (int) number;
    }

    public int reverse16(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse17(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        ArrayList<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }

    public int reverse18(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;
        
        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y/10;
        }
        
        int number = 0;
        int length = digits.size();
        
        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length-i-1);
        }
        
        if (number >= Math.pow(2, 31)) {
            return 0;
        }
        
        number = sign == 1 ? -number : number;
        return (int) number;
    }

    public int reverse19(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return (int)number;
    }

    public int reverse20(int x) {
        int sign = x < 0 ? 1 : 0;
        int y = x < 0 ? -x : x;

        List<Integer> digits = new ArrayList<>();
        while (y > 0) {
            int reminder = y % 10;
            digits.add(reminder);
            y = y / 10;
        }

        int number = 0;
        int length = digits.size();

        for (int i = 0; i < length; i++) {
            number += digits.get(i) * Math.pow(10, length - i - 1);
        }

        if (number >= Math.pow(2, 31)) {
            return 0;
        }

        number = sign == 1 ? -number : number;
        return number;
    }
}


