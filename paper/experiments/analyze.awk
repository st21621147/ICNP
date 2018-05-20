BEGIN{FS="|"} 

{
  T=$1; ID=$3; RES=$NF; 
  split(T,a,":"); T1=sprintf("%.3f",a[1]*3600+a[2]*60+a[3]); 
  n=split(RES,a," "); 
  if (n==1) 
     print T1,ID,RES,"0"; 
  else 
     print T1,ID,a[1],"1";
}

