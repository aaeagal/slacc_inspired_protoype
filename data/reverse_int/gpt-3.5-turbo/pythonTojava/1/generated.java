import java.util.ArrayList;
import java.util.List;

class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;
import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

public class Solution {
    public int reverse(int x) {
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


import java.lang.Math;

public class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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


import java.lang.Math;

public class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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


import java.util.ArrayList;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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
}


import java.lang.Math;

class Solution {
    public int reverse(int x) {
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


