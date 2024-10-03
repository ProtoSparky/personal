using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NAudio.CoreAudioApi;
using NAudio.Wave;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Runtime.CompilerServices;


namespace test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string string_test = "this is a test";
            string string_test_2 = " 5120"; 
            var tester = new test_class();
            tester.test_object(string_test, string_test_2, out string string_test_new, out string string_test_2_new);
            string_test = string_test_new;
            string_test_2 = string_test_2_new;
            Console.WriteLine(string_test);
            Console.WriteLine(string_test_2);
            Console.ReadLine();
        }
    }
    public class test_class
    {
        public void test_object(string string_test, string string_test_2, out string string_test_new, out string string_test_2_new)
        {
            Console.WriteLine(string_test);
            Console.WriteLine(string_test_2); 
            string_test_new = "this is a better test";
            string_test_2_new = "no u:3"; 
            
        }
    }
}
