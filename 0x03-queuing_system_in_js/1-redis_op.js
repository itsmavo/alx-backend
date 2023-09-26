import { createClient, print } from "redis";

const client = createClient({
    legacyMode: true
});
client.connect();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (_err, reply) => {
        console.log(reply);
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')

