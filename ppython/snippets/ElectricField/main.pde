public class Tool
{Vector addV(Vector i,Vector j)
  {
    return new Vector(0,0,i.l+j.l);
  }
  Vector add(Vector i,Vector j)
  {
    float x = i.l*i.x+j.l*j.x;
    float y = i.l*i.y+j.l*j.y;
    float l = sqrt(x*x+y*y);
    Vector v = new Vector(x/l,y/l,l);
    return v;
  }
  void drawArrow(int x, int y,float l, float vx, float vy)
  {
    stroke(0.1);
    if(true)
    {
      float x2 = x+10*vx;
      float y2 = y+10*vy;
      line(x,y,x2,y2);
  }
    
  }
}
