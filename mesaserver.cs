using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using UnityEngine;
using UnityEngine.Networking;

public class mesaserver : MonoBehaviour
{
    public GameObject car;
    Vector3[] coords;
    private Rigidbody rigidbody;
    string coordString;
    List<GameObject> cars = new List<GameObject>();
    private GameObject tempcar;

    // Start is called before the first frame update
    void Start()
    {
        List<Vector3> posiciones = new List<Vector3>();
        posiciones.Add(new Vector3(2, 1, 20)); // 0
        posiciones.Add(new Vector3(6, 1, 18)); // 1
        posiciones.Add(new Vector3(11, 1, 19)); // 2

        posiciones.Add(new Vector3(9, 1, 21)); // 3
        posiciones.Add(new Vector3(8, 1, 15)); // 4
        for (int i = 0; i < 5; i++)
        {
            GameObject c = Instantiate(car, posiciones[i], Quaternion.identity);
            cars.Add(c);
        }
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        StartCoroutine(GETPos());

    }

    IEnumerator GETStartPos()
    {

        using (UnityWebRequest www = UnityWebRequest.Get("http://localhost:5000/api/model/5"))
        {
            yield return www.SendWebRequest();
            if (www.result != UnityWebRequest.Result.Success)
            {
                print(www.error);
            }
            else
            {
                //print("Respuesta de server: " + www.downloadHandler.text);
                coordString = www.downloadHandler.text;
            }
        }
        coordString = coordString.Replace("[", "").Replace("]", "");
        string[] substrings = coordString.Split(',');

        coords = new Vector3[substrings.Length / 2];

        for (int i = 0; i < substrings.Length; i += 2)
        {
            Vector3 coord = new Vector3(float.Parse(substrings[i]), 1, float.Parse(substrings[i + 1]));

            coords[i / 2] = coord;
        }
        int size = coords.Length;
        for (int i = 0; i < size; i++)
        {
            GameObject c = Instantiate(car, coords[i], Quaternion.identity);
            cars.Add(c);
        }
    }

    IEnumerator GETPos()
    {

        using (UnityWebRequest www = UnityWebRequest.Get("http://localhost:5000/api/model/5"))
        {
            yield return www.SendWebRequest();
            if (www.result != UnityWebRequest.Result.Success)
            {
                print(www.error);
            }
            else
            {
                //print("Respuesta de server: " + www.downloadHandler.text);
                coordString = www.downloadHandler.text;
            }
        }
        coordString = coordString.Replace("[", "").Replace("]", "");
        string[] substrings = coordString.Split(',');

        coords = new Vector3[substrings.Length/2];

        for (int i = 0; i < substrings.Length; i += 2)
        {
            Vector3 coord = new Vector3(float.Parse(substrings[i]), 1, float.Parse(substrings[i + 1]));

            coords[i / 2] = coord;
        }
        for(int i =0;i<5;i++)
        {
            tempcar = cars[i];
            rigidbody = tempcar.GetComponent<Rigidbody>();
            rigidbody.MovePosition(coords[i]);
        }
    }
}
