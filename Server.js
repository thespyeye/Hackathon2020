let express = require('express');
let app = express();
let bodyParser = require('body-parser');

var result = "N"

var dataa

var light_val = 0

function sleep(milliseconds){
	const date = Date.now();
	let currentDate = null;
	do{
		currentDate = Date.now();
	} while (currentDate - date < milliseconds);
	
}

//ar dataaa = {id: "Zoom",
//				meet: '1'}

app.use(bodyParser.urlencoded({extended : true}));

app.get('/', function(req, res){
res.send('<h1> Blah blah blah somthing about javascript <h1>');

});

app.get('/nano', function(req, res){
res.send(light_val);
});

app.listen(3000, function(){
console.log("Da server is up. Yay. Go to 192.168.1.127:3000 for a blank page with some words on it");
});

app.post('/data', (req, res) => {
	
	res.send("Ack'd");
	dataa = req['body']
	console.log(dataa);
	if (dataa == {'Status': 'no'}){
		light_val = '0';
		
	}
	if(dataa == {'Status': 'yes'}){
		light_val = '1';
		
	}
});
app.put('/data', (req, res) => {
	var zoom = 'Zoom'
	res.write("Hello")
	res.send("Ack'd");
	
});
const readline = require("readline");
const r1 = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

sleep(500);
r1.question("Do you wish to terminate the server? Y/N", function(result){
if(result == "Y"){
	process.exit();
	
}	
	
});