using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandTracking : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive UdpReceive;
    public GameObject[] handPoints;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = UdpReceive.data;
        data = data.Remove(0, 1);
        data = data.Remove(data.Length-1, 1);
       // print(data);
        string[] points = data.Split(',');
       // print(points[0]);
        
        //print(data);
        //print(points[0]);

        float initalDistance = Vector3.Distance(handPoints[5].transform.localPosition, handPoints[0].transform.localPosition);
        float minScale = 0.01f; // minimalna skala prefabu
        float scaleFactor  = 0.1f; // współczynnik skalowania 
        for (int i = 0; i < 21; i++)
        {
            float x = 7 - float.Parse(points[i * 3]) / 100;
            float y = float.Parse(points[i * 3 + 1]) / 100;
            float z = float.Parse(points[i * 3 + 2]) / 100;
            
            handPoints[i].transform.localPosition = new Vector3(0, 0, z / initalDistance);

            float newScale = Mathf.Max(minScale, 1.0f - (initalDistance - z) * scaleFactor);
            handPoints[i].transform.localScale = new Vector3(newScale, newScale, newScale);

            handPoints[i].transform.localPosition = new Vector3(x, y, 0);
            // handPoints[i].transform.localScale = new Vector3(newScale, newScale, newScale);

        }
            //float W = 100;
            //float d = 40;
            //double f = 0.79;
            //float d = (float) (W * f) / handZ;
            //print(d);
            //float f = 62;
            //float newZ = currentPos.z + z;
            //Vector3 lastZ = new Vector3(0, 0, z * d);
            //handPoints[i].transform.localPosition = new Vector3(x,y,z);

            


        }
            
    }

