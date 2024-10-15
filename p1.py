#include <DHT.h>
#define DHTPIN 6
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
float h=0;
float t=0;
const int beats = 7;
const int key = A0;
const int dc1=2;  
const int dc2=3;
const int dc3=4;
const int dc4=5;
char x=0;
int   count=0;
int   i=0;
int   j=0;
int   ppp=0;
void setup()
{
  pinMode(dc1,OUTPUT);
  pinMode(dc2,OUTPUT);
  pinMode(dc3,OUTPUT);    
  pinMode(dc4,OUTPUT);
  pinMode(key,INPUT);  
  pinMode(beats,INPUT);  
  Serial.begin(9600);
  digitalWrite(dc1,LOW);
  digitalWrite(dc2,LOW);
  digitalWrite(dc3,LOW);  
  digitalWrite(dc4,LOW);
  digitalWrite(key,HIGH);
  dht.begin();
  Serial.begin(9600);
  Serial.println("WELCOME");
}
void loop()
{
  if(digitalRead(key)==LOW)
  {
  Serial.println("SENSORS READING STARTED");    
//  for(j=0;j<=22;j++)
//  {
  for(i=0;i<=50;i++)
  {    
  t = dht.readTemperature();
  delay(100);  
  if(digitalRead(beats)== LOW)
  {
  ppp=1;
  }
  delay(100);
  if(digitalRead(beats)== HIGH)
  {
    if(ppp==1)
    {
    count=count+1;
    Serial.println(count);
    ppp=0;
    }
  }
  }
  Serial.print("PATIENT TEMPERATURE IS:");  
  Serial.print(t);
  Serial.println("C");
  count=(count*6);
  Serial.print("PATIENT HEART RATE IS:");  
  Serial.print(count);
  Serial.println("BPM");  
  count=0;  
  }
//}

  if(Serial.available()>0)  // Send data only when you receive data:
  {
    x = Serial.read();      //Read the incoming data and store it into variable data
    if(x == 'B')            
    {
    digitalWrite(dc2,HIGH);  
    digitalWrite(dc1,LOW);    
    digitalWrite(dc4,HIGH);  
    digitalWrite(dc3,LOW);
    Serial.println("BACK");      
    }
    if(x == 'F')            
    {
    digitalWrite(dc2,LOW);  
    digitalWrite(dc1,HIGH);    
    digitalWrite(dc4,LOW);  
    digitalWrite(dc3,HIGH);
    Serial.println("FORWARD");    
    }
    if(x == 'L')            
    {
    digitalWrite(dc2,LOW);  
    digitalWrite(dc1,HIGH);    
    digitalWrite(dc4,HIGH);  
    digitalWrite(dc3,LOW);
    Serial.println("LEFT");    
    }
    if(x == 'R')            
    {
    digitalWrite(dc2,HIGH);  
    digitalWrite(dc1,LOW);    
    digitalWrite(dc4,LOW);  
    digitalWrite(dc3,HIGH);
    Serial.println("RIGHT");    
    }
    if(x == 'S')            
    {
    digitalWrite(dc1,LOW);  
    digitalWrite(dc2,LOW);    
    digitalWrite(dc3,LOW);  
    digitalWrite(dc4,LOW);
    Serial.println("STOP");    
    }
    }        
}