GridSize = 32;
GridHeight = 4;
GridsX = 50;
GridsY = 15;

difference(){
    
cube([(GridsY*GridSize)+(GridsY*5)+5, (GridsX*GridSize)+(GridsX*5)+5, GridHeight]);
    
for (i = [1:1:GridsY]) {
 for (j = [1:1:GridsX]){
     translate([((i*GridSize)+i*5)-(GridSize),((j*GridSize)+j*5)-(GridSize), -1])
     cube([GridSize,GridSize,GridHeight+2]);
     }
    };
}
    


