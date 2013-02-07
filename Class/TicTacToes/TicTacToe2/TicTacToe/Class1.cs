using System;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;

namespace TicTacToe
{
    public class Board
    {
        // Class Data
        private string[] grid = new string[9] {"","","","","","","","",""};
        private string[] winStates = new string[8] {"012", "345", "678", "036", "147", "258", "048", "246"};

        public bool isWin()
        {
            string stateX = "X";
            string stateO = "O";

            for (int i = 0; i < 8; i++)
            {
                int x1 = Convert.ToInt32(winStates[i].Substring(0,1));
                int x2 = Convert.ToInt32(winStates[i].Substring(1,2));
                int x3 = Convert.ToInt32(winStates[i].Substring(2,3));

                if (grid[x1] == stateX && grid[x2] == stateX && grid[x3] == stateX)
                {
                    return true;
                }
                else if (grid[x1] == stateO && grid[x2] == stateO && grid[x3] == stateO)
                {
                    return true;
                }
            }

            return false;
        }

        public override string ToString() 
        {
            string board = "";
            board += grid[0] + "|" + grid[1] + "|" + grid[2] + "\n";
            board += grid[3]+"|"+grid[4]+"|"+grid[5]+"\n";
            board += grid[6]+"|"+grid[7]+"|"+grid[8]+"\n";
            return board; 
        }
        
    }
}
