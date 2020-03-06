class Body
{
  int x,y;
  float charge;
  Body(int x,int y)
  {
    this.x = x;
    this.y = y;
    charge = 1;
    
  }
  public void move()throws Exception
  {
    Vector v= new Vector(0,0,0);
    
    for(int i = 0;i<s.bodies.length;i++)
      {
        
        if(s.bodies[i]!=this)
        {
         
         Body b = s.bodies[i];
         float ln = dist(b.x,b.y,x,y);
         v=new Tool().add(v,new Vector((x-b.x)/ln,(y-b.y)/ln,Field.k*charge*b.charge/(ln*ln)));
      }
       
    }
        x += v.l*v.x*5;//speed
        y += v.l*v.y*5;//speed
        if(bs[0] == this)
        println(v.l*v.x*100+"\t"+y);
  }
  Body(int x,int y,float charge)
  {
    this.x = x;
    this.y = y;
    this.charge = charge;
  }
  
}
