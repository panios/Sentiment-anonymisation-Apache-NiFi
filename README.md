#  Privacy preserving sentiment analysis with NiFi
The page includes code, NiFi flowfiles and additional documentation for the paper: Privacy preserving sentiment analysis on multiple edge data streams with Apache NiFi


**Table I.** 	HARDWARE AND SOFTWARE SETUP

| Name          | Machine       | Specs         |Services       |
| ------------- | ------------- | ------------- |-------------  |
| Cloud Node| Mac mini, macOS Sierra 10.12.6 |2,6 GHz Intel Core i5,8 GB 1600 MHz DDR3 |Nifi 1.5; Minifi-toolkit0.6; Elasticsearch/Kibana 5.6|
|Regional Note|	macOS Sierra 10.12.6 	|2,6 GHz Intel Core i5,8 GB 1600 MHz DDR3	|Nifi 1.5; Minifi-toolkit 0.6; Elasticsearch/Kibana 5.6|
|Edge1|	Raspberry Pi 3B (Sony UK), Debian 9.8|	1GB RAM, ARMv7	|Minifi 0.5| 
|Edge2|	Raspberry Pi 3B (Sony UK) + Sense Hat, Debian 9.8|	1GB RAM, ARMv7	|Minifi 0.5|
|Edge3|	Raspberry Pi 3B (Sony UK) + Voice Hat, Debian 9.8|	1GB RAM, ARMv7	|Minifi 0.5|


![alt text](https://github.com/PanosKostakos/Sentiment-anonymisation-Apache-NiFi/blob/master/img/Edge_cluster.png)  

![alt text](https://github.com/PanosKostakos/Sentiment-anonymisation-Apache-NiFi/blob/master/img/algorithmic_representation_MINIFI%20.png)  

![alt text](https://github.com/PanosKostakos/Sentiment-anonymisation-Apache-NiFi/blob/master/img/dataflow.png)  


