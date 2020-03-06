Space s;
Body[] bs;
int freq = 20;
void setup()
{
  int n = 3;
  size(1000,1000);
  bs = new Body[n];
  for(int i = 0;i<n;i++)
  {
    //bs[i] = new Body((int)random(0,width),(int)random(0,height),10);
  }
  bs[0] = new Body(500,500,10);
  bs[1] = new Body(700,500,10);
  bs[2] = new Body(600,(int)(500+100*sqrt(3)),10);
  //bs[n] = new Body(width/2,height/2,-50);
  //bs[3] = new Body(10,10,0);
  s = new Space(bs);;
  //setupi();
}
void setupi()
{
  
    background(0);
    noStroke();
    
     for(int i = 1;i<width;i+=2)
    for(int j = 1;j<height;j+=2){
    
          Field f = new Field(i,j,s);
      Vector v = f.getPotential();
      try
      {
        float a = map(v.getL()*10,-1000,1000,0,150)+30;
        //if(i==190&&j==190)
        ///print(a);
        fill(a*abs((sin(freq*a)+3)),a*abs((sin(freq*a)+3)),0);
       
      }
      catch(Exception e){}
      ellipse(i,j,10,10);
    }
    
    
  for(int i = 1;i<width;i+=8)
    for(int j = 1;j<height;j+=8)
{
    Field f = new Field(i,j,s);
      Vector v1 = f.getFieldVector();
      if(abs(f.getPotential().l)<500)
        new Tool().drawArrow(i,j,v1.l,v1.x,v1.y);
    }
    for(Body b: bs)
      {
        fill(255);
      ellipse(b.x,b.y,10,10);
    }
}
void draw()
{try{setupi();
  for(int i = 0;i<bs.length;i++)
  {
  // bs[i].move();
  }
}
catch(Exception e)
{}
}
