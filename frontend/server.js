const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const http = require('http');
const app = express();
var redis = require("redis"),
    client = redis.createClient();

client.on("error", function (err) {
    console.log("Error " + err);
});

var fakenews = true;
var ecuData = {'RPM':0, 'SPEED':0};
var refreshInterval = 16.6;

// Parsers
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

// Angular DIST output folder
app.use(express.static(path.join(__dirname, 'dist')));

app.route('/api/dash').get((req, res) => {
    res.send({
        dash: [{ speed: '100' }]
    });
});

// Send all other requests to the Angular app
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'dist/index.html'));
});

//Set Port
const port = process.env.PORT || '4200';
app.set('port', port);

const server = http.createServer(app);

server.listen(port, () => console.log(`Running on 0.0.0.0:${port}`));

// Socket.IO part
var io = require('socket.io')(server);

io.on('connection', function (socket) {
    console.log('New client connected!');
    console.log(Object.keys(ecuData));

    //send data to client
    setInterval(function() {

        // simulating/testing on a desktop
        if (fakenews) {
            if (ecuData['RPM'] < 7200) {
                ecuData['RPM'] += 11;
            } else {
                ecuData['RPM'] = 0;
            }
            if (ecuData['SPEED'] < 120) {
                ecuData['SPEED'] += 1;
            } else {
                ecuData['SPEED'] = 0;
            }
        }
        // real deployment
        else {
            client.ping(function (err, pong) {
                // reply is "PONG" if the redis server is reachable
                if (pong == "PONG") {
                    // update OBKEYS in redis
                    client.set('OBDKEYS', Object.keys(ecuData).join(':'));

                    // update every value in dictionary
                    Object.keys(ecuData).forEach(function(key) {
                        client.get(key.trim(), function(error, reply) {
                            if (reply == null) {
                                console.log("Warn: \'", key.trim(), "\' is null");
                                reply = "0.0"; // if null, force to 0
                            }
                            else if (isNaN(parseFloat(reply))) {
                                console.log("Warn: \'", key.trim(), "\' with reply \'", reply.trim(), "\' is NaN");
                                reply = "0.0"; // if not parsable, force to 0
                            }

                            // finally set the dictionary value
                            ecuData[key.trim()] = Math.floor(parseFloat(reply));
                        });
                    });
                }
                else {
                    console.log("Error: Redis not available");
                }
            });
        }

        socket.emit('ecuData', ecuData);
    }, refreshInterval);
});
