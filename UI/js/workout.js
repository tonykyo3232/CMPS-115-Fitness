//********************
// global variable
//********************

//Declare Styles
var style_NA = ["NA"];
var style_BB = ["Body-Building"];
var style_PL = ["Power-Lifting"];
var style_GF = ["General-Fitness"];
var style_BB_PL = ["Body-Building", "Power-Lifting"];
var style_BB_GF = ["Body-Building", "General-Fitness"];
var style_PL_GF = ["Power-Lifting", "General-Fitness"];
var style_ALL = ["Body-Building", "Power-Lifting", "General-Fitness"];
//Declare Goals
var goal_NA = ["NA"];
var goal_LW = ["Lose-Weight"];
var goal_BM = ["Build-Muscle"];
var goal_BS = ["Build-Strength"];
var goal_LW_BM = ["Lose-Weight", "Build-Muscle"];
var goal_LW_BS = ["Lose-Weight", "Build-Strength"];
var goal_BM_BS = ["Build-Muscle", "Build-Strength"];
var goal_ALL = ["Lose-Weight", "Build-Muscle", "Build-Strength"];
//Declare Routines
var routine_NA = ["NA"];
var routine_LEG = ["Leg"];
var routine_ARM = ["Arm"];
var routine_BACK = ["Back"];
var routine_CHEST = ["Chest"];
var routine_LA = ["Leg", "Arm"];
var routine_LB = ["Leg", "Back"];
var routine_LC = ["Leg", "Chest"];
var routine_LAB = ["Leg", "Arm", "Back"];
var routine_AB = ["Arm", "Back"];
var routine_AC = ["Arm", "Chest"];
var routine_BC = ["Back", "Chest"];
var routine_ALL = ["Leg", "Arm", "Back", "Chest"];


//Define Classes
Class Workout_Program{
	constructor(Name, Level, Length, Style[], Goal[], Routine[]){
		this.Name = Name;
		this.Level = Level;
		this.Length = Length;
		this.Style[] = Style[];
		this.Goal[] = Goal[];
		this.Routine[] = Routine[];
	}
	
	
	
	get Name(){
		return this.Name;
	}
	
	get Level(){
		return this.Level;
	}
	
	get Length(){
		return this.Length;
	}
	
	get Style(){
		return this.Style[];
	}
	
	get Goal(){
		return this.Goal[];
	}
	
	get Routine(){
		return this.Routine[];
	}
	
	
}


//Create Workout Program Objects
My_Beginner_Program = new Workout_Program("My Beginner Program", "Beginner", "5-8", style_GF, goal_BM, routine_ALL);
Combo_Program = new Workout_Program("Combo Program", "Advance", "9+", style_PL, goal_BM_BS, routine_ALL);
Summer_Program = new Workout_Program("Get Ready For Summer Program", "Intermediate", "5-8", style_BB), goal_BM, routine_ALL;
Big_Arm_Routine = new Workout_Program("Big Arm Routine", "Intermediate", "NA", style_NA, goal_BM);
Massive_Leg_Routine = new Workout_Program("Massive Leg Routine", "Beginner", "NA", style_NA, goal_BM_BS, routine_LEG);