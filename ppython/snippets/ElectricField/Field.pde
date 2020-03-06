class Field
{
  static final float k = 10;
  Body[] bodies;
  Space s;
  int x;
  int y;
  
  Field(int x,int y,Space s)
  {
      this.bodies = s.bodies;
      this.s = s;
      this.x = x;
      this.y = y;
  }
  Vector getPotential()
  {
    Vector[] vs = new Vector[bodies.length];
    for(int i = 0;i<bodies.length;i++)
    {
      Body b = bodies[i];
      float l = k*b.charge/pow((dist(x,y,b.x,b.y)),1);/*
      float xi = abs(l)/l*((b.x-x)/dist(x,y,b.x,b.y));
      float yi = abs(l)/l*((b.y-y)/dist(x,y,b.x,b.y));*/
      vs[i] = new Vector(0,0,l);
    }
    Tool l = new Tool();
    for(int i = 1;i<vs.length;i++)
    {
      vs[i] = l.addV(vs[i],vs[i-1]);
    }
    return vs[vs.length-1];
  }
  Vector getFieldVector()
  {Vector[] vs = new Vector[bodies.length];
    for(int i = 0;i<bodies.length;i++)
    {
      Body b = bodies[i];
    float l = k*b.charge/pow((dist(x,y,b.x,b.y)),2);     
    float xi = ((x-b.x)/dist(x,y,b.x,b.y));
    float yi = ((y-b.y)/dist(x,y,b.x,b.y));
    vs[i] = new Vector(xi,yi,l);
    }
    for(int i = 1;i<vs.length;i++)
    {
      vs[i] = new Tool().add(vs[i],vs[i-1]);
    }
    return vs[vs.length-1];  
}
  
}
