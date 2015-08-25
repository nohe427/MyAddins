//
//  main.cpp
//  HappyNumber
//
//  Created by Alexander Nohe on 8/6/15.
//  Copyright (c) 2015 Alexander Nohe. All rights reserved.
//

#include <iostream>



class Solution
{
public:
    static bool isHappy(int n)
    {
        std::string x = std::to_string(n);
        for (int i = 0; i < x.length(); i++) {
            int a;
            std::string k = &x[i];
            std::cout << k;
            a = stoi(k);
            std::cout << a << "..\n";
            //int z = multiply(int(x[i]));
            //std::cout << z << std::endl;
        }
        return true;
    }
    
private:
    static int multiply(int z)
    {
        int x = z * z;
        return x;
    }
    
    static int stoi( const std::string& str, std::size_t* pos = 0, int base = 10 )
    {
        const char* begin = str.c_str() ;
        char* end = nullptr ;
        long value = std::strtol( begin, &end, base ) ;
        
        if( errno == ERANGE || value > std::numeric_limits<int>::max() )
            throw std::out_of_range( "stoi: out ofrange" ) ;
        
        if( end == str.c_str() )
            throw std::invalid_argument( "stoi: invalid argument" ) ;
        
        if(pos) *pos = end - begin ;
        
        return value ;
    }
    
};

int main(int argc, const char * argv[]) {
    // insert code here...
    Solution::isHappy(56);
    return 0;
}
