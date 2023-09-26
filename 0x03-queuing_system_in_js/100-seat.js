import { createClient } from "redis";
import express  from 'express';
import { promisify } from 'util';
import { createQueue } from "kue";

const app = express();

const client = createClient();

const queue = createQueue();

client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const get = promisify(client.get).bind(client);

const reserveSeat = (number) => {
    client.set('available_seats', number);
}

const getCurrentAvailableSeats = async () => {
    const seats = await get('available_seats');
    return seats;
}

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({"numberOfAvailableSeats": availableSeats});
});

app.get('/reserve_seat', (req, res) => {
    if(!reservationEnabled) {
        res.json({"status": "Reservation are blocked"});
        return;
    }
    const job = queue.create('reserve_seat', {'seat': 1}).save((error) => {
        if(error) {
            res.json({"status": "Reservation in process"});
            job.on('complete', () => {
                console.log(`Seat reservation job ${job.id} completed`);
            }).on('failed', (error) => {
                console.log(`Seat reservation job ${job.id} failed: ${error}`);
            });
        }
    });
});

app.get('/process', (req,res) => {
    res.json({"status": "Queue processing"});
    queue.process('reserve_seat', async (job,done) => {
        const seat = Number(await getCurrentAvailableSeats());
        if (seat === 0) {
            reservationEnabled = false;
            done(Error('Not enough seats available'));
        } else {
            reserveSeat(seat - 1);
            done();
        }
    });
});

const port = 1245;
app.listen(port, () => {
    console.log(`app is listening http://localhost:${port}`);
});
reserveSeat(50);