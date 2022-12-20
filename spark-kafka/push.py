from kafka import KafkaProducer
from kafka.errors import KafkaError
import asyncio
import json


def main():
	topic = "topic"
	producer = KafkaProducer(bootstrap_servers=['localhost:29092', 'localhost:39092'],
							 value_serializer=lambda m: json.dumps(m).encode('ascii'))

	key = input("Key: ")
	value = input("Value: ")
	future = producer.send(topic, {key : value})

	try:
		record_metadata = future.get(timeout=10)

	except KafkaError:
		pass

	print(record_metadata.topic)
	print(record_metadata.partition)
	print(record_metadata.offset)


if __name__ == "__main__":
	main()