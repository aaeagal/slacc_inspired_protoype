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
    // main method

    // main method
    public static void main(String[] args) {
        // get the input from the user and call the function
        String methodName = args[0];

        int x = Integer.parseInt(args[1]);

        Solution solution = new Solution();

        switch (methodName) {
            case "reverse1":
                System.out.println(solution.reverse1(x));
                break;
            case "reverse2":
                System.out.println(solution.reverse2(x));
                break;
            case "reverse3":
                System.out.println(solution.reverse3(x));
                break;
            case "reverse4":
                System.out.println(solution.reverse4(x));
                break;
            case "reverse5":
                System.out.println(solution.reverse5(x));
                break;
            case "reverse6":
                System.out.println(solution.reverse6(x));
                break;
            case "reverse7":
                System.out.println(solution.reverse7(x));
                break;
            case "reverse8":
                System.out.println(solution.reverse8(x));
                break;
            case "reverse9":
                System.out.println(solution.reverse9(x));
                break;
            case "reverse10":
                System.out.println(solution.reverse10(x));
                break;
            case "reverse11":
                System.out.println(solution.reverse11(x));
                break;
            case "reverse12":
                System.out.println(solution.reverse12(x));
                break;
            case "reverse13":
                System.out.println(solution.reverse13(x));
                break;
            case "reverse14":
                System.out.println(solution.reverse14(x));
                break;
            case "reverse15":
                System.out.println(solution.reverse15(x));
                break;
            case "reverse16":
                System.out.println(solution.reverse16(x));
                break;
            case "reverse17":
                System.out.println(solution.reverse17(x));
                break;
            case "reverse18":
                System.out.println(solution.reverse18(x));
                break;
            case "reverse19":
                System.out.println(solution.reverse19(x));
                break;
            case "reverse20":
                System.out.println(solution.reverse20(x));
                break;
        }

        




    }
}


