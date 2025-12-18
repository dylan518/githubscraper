
import java.util.ArrayList;
import java.util.List;
import java.util.LinkedList;
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Bayan
 */
public class BFSAlgo 
{
    List<Edges> Ed;
    public BFSAlgo(List<Vertex> V ,List<Edges> E)
    {
        Ed=E;
        
    }
    public void BFS(Vertex S)
    {
        LinkedList<Vertex> u=new LinkedList<Vertex>();
        u.add(S);
        while(!u.isEmpty())
        {
        S=u.removeFirst();
        visited(S);
        for(int i=0;i<getadj(S).size();i++)
        { ArrayList<Vertex> w=new ArrayList<Vertex>();
           w=(ArrayList<Vertex>) getadj(S);
        if(w.get(i).visit == false)
        {u.add(w.get(i));
        
        }
        }
        }
        }
        
    
    
    public void visited(Vertex v)
    {
     v.visit=true;
    }
    public List<Vertex> getadj(Vertex x)
    {  
        ArrayList<Vertex> l= new ArrayList<Vertex>();
        for(int i=0;i<Ed.size();i++)
        {
          if(Ed.get(i).Start==x)
             l.add(x);
          if(Ed.get(i).End==x)
             l.add(x);
        }
        
            return l;
    }
}
