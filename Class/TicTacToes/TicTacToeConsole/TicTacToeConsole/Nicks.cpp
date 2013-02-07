#include "stdafx.h"
//#include<iostream>
//#include<iomanip>
//
//using namespace std;
//
//const int ROW=3;
//const int COL=3;
//
//char mark[ROW][COL];
//
////============================================================================================================
////function 1: "initialize"- initializes the values in mark to make the grid display look appropriate
////============================================================================================================
//void initialize()
//{
//	//every mark except for those on the bottom row is initialized to '_'
//	for(int row=0; row<ROW-1; row++)
//	{
//		for(int col=0; col<COL; col++)
//			mark[row][col]='_';
//	}
//
//	//the bottom row is initialized to ' '
//	for(int col=0; col<COL; col++)
//		mark[ROW-1][col]=' ';
//
//}
////============================================================================================================
////end of function 1
////============================================================================================================
//
//
//
////============================================================================================================
////function 2: "printBoard"- prints a ROWxCOL grid populated by the present values in the mark array
////============================================================================================================
//void printBoard()
//{
//	int col;				//column counter
//	int row;				//row counter
//
//	//indent column markers
//	cout<<"             ";
//
//	//set column markers
//	for(int i=1; i<=COL; i++)
//		cout<<i<<"   ";
//
//	//indent row 1
//	cout<<"\n\n         ";
//
//	//print ROW-1xCOL grid populated by the present values in the mark array
//	for(row=0; row<ROW-1; row++)
//	{
//		cout<<row+1<<"  ";		//set row marker
//
//		//print each column
//		for(col=0; col<COL; col++)
//		{
//			cout<<"_"<<mark[row][col]<<(col==(COL-1)? "_" : "_|");
//		}
//		cout<<"\n         ";
//	}
//
//	//print the final row
//	row=ROW-1;
//	cout<<row+1<<"  ";
//	for(col=0; col<COL; col++)
//		cout<<" "<<mark[row][col]<<(col==COL-1? " " : " |");
//}
////============================================================================================================
////end function 2
////============================================================================================================
//
//
//int validate(int row, int col)
//{
//	int valid=1; 
//
//	if(row>ROW || col>COL || row<1 || col<1)
//		valid=0;
//	else if(mark[row-1][col-1]!=' ' && mark[row-1][col-1]!='_')
//		valid=0;
//
//	return valid;
//}
//
//int checkWin()
//{
//	int win=0;
//	int row=0;
//	int col=0;
//	int fallout=0;
//	
//	while(win!=1 &&  row<ROW)
//	{
//		while(col<COL-1 && fallout!=1)
//		{
//			if( (mark[row][col]==mark[row][col+1]) && ((mark[row][col]!=' ') && (mark[row][col]!='_')) )
//				win=1;
//			else
//			{
//				win=0;
//				fallout=1;
//			}
//
//			col++;
//		}
//
//		row++;
//		col=0;
//		fallout=0;
//	}
//	
//
//	if(win==1)
//		return win;
//
//	row=0;
//	
//	
//	while(win!=1 && col<COL)
//	{
//		while(row<ROW-1 && fallout!=1)
//		{
//			if( (mark[row][col]==mark[row+1][col])  && ((mark[row][col]!=' ') && (mark[row][col]!='_')) )
//				win=1;
//			else
//			{
//				win=0;
//				fallout=1;
//			}
//
//			row++;
//		}
//
//		col++;
//		row=0;
//		fallout=0;
//	}
//	
//	if(win==1)
//	return win;
//
//
//	col=0;
//
//	
//	while(row<ROW-1 && fallout!=1)
//	{
//		if( (mark[row][col]==mark[row+1][col+1])  && ((mark[row][col]!=' ') && (mark[row][col]!='_')) )
//			win=1;
//		else
//		{
//			win=0;
//			fallout=1;
//		}
//
//		row++;
//		col++;
//	}
//	
//	if(win==1)
//		return win;
//
//	col=COL-1;
//	row=0;
//	fallout=0;
//
//
//	while(row<ROW-1 && fallout!=1)
//	{
//		if( (mark[row][col]==mark[row+1][col-1])  && ((mark[row][col]!=' ') && (mark[row][col]!='_')) )
//			win=1;
//		else
//		{
//			win=0;
//			fallout=1;
//		}
//
//		row++;
//		col--;
//	}
//	
//	return win;
//
//}
//
//
//
//int checkFull()
//{
//	int i=0;
//
//	for(int row=0; row<ROW; row++)
//	{
//		for(int col=0; col<COL; col++)
//			if(mark[row][col]!=' ' && mark[row][col]!='_')
//				i++;
//	}
//
//	if(i==(ROW*COL))
//		return 1;
//	else 
//		return 0;
//}
//
//
//int main()
//{
//	int player=2;
//	int row=0;
//	int col=0;
//
//	initialize();
//
//	while(checkWin()!=1 && checkFull()!=1)
//	{
//
//		player==2? player=1 : player=2;
//		printBoard();
//		cout<<"\n\nPlayer "<<player<<" make a move: ";
//		cin>>row>>col;
//
//		while(validate(row,col)!=1)
//		{
//			cout<<"\n\nYou fail at life. Make a valid move byitch.\n\n";
//			cin>>row>>col;
//		}
//		if(player==1)
//			mark[row-1][col-1]='x';
//		else
//			mark[row-1][col-1]='o';
//
//		checkWin();
//		checkFull();
//		system("cls");
//	}
//
//	if(checkWin()==1)
//		cout<<"Player "<<player<<" wins. Good job them.\n";
//	else
//		cout<<"Awww you both lose. If only one of you weren't awful at life.\n";
//	cout<<"\n\n\nPress enter to exit the program...";
//	cin.ignore();
//	cin.get();
//}