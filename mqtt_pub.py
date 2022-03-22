import paho.mqtt.client as mqtt
pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print('Broker connected')
pub_client.publish('gpcet/ai'/,'hi')