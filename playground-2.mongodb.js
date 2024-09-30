// /* global use, db */
// // MongoDB Playground
// // To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// // Make sure you are connected to enable completions and to be able to run a playground.
// // Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// // The result of the last command run in a playground is shown on the results panel.
// // By default the first 20 documents will be returned with a cursor.
// // Use 'console.log()' to print to the debug output.
// // For more documentation on playgrounds please refer to
// // https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// // Select the database to use.
// use('mongodbVSCodePlaygroundDB');

// // Insert a few documents into the sales collection.
// db.getCollection('sales').insertMany([
//   { 'item': 'abc', 'price': 10, 'quantity': 2, 'date': new Date('2014-03-01T08:00:00Z') },
//   { 'item': 'jkl', 'price': 20, 'quantity': 1, 'date': new Date('2014-03-01T09:00:00Z') },
//   { 'item': 'xyz', 'price': 5, 'quantity': 10, 'date': new Date('2014-03-15T09:00:00Z') },
//   { 'item': 'xyz', 'price': 5, 'quantity': 20, 'date': new Date('2014-04-04T11:21:39.736Z') },
//   { 'item': 'abc', 'price': 10, 'quantity': 10, 'date': new Date('2014-04-04T21:23:13.331Z') },
//   { 'item': 'def', 'price': 7.5, 'quantity': 5, 'date': new Date('2015-06-04T05:08:13Z') },
//   { 'item': 'def', 'price': 7.5, 'quantity': 10, 'date': new Date('2015-09-10T08:43:00Z') },
//   { 'item': 'abc', 'price': 10, 'quantity': 5, 'date': new Date('2016-02-06T20:20:13Z') },
// ]);

// // Run a find command to view items sold on April 4th, 2014.
// const salesOnApril4th = db.getCollection('sales').find({
//   date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') }
// }).count();

// // Print a message to the output window.
// console.log(`${salesOnApril4th} sales occurred in 2014.`);

// // Here we run an aggregation and open a cursor to the results.
// // Use '.toArray()' to exhaust the cursor to return the whole result set.
// // You can use '.hasNext()/.next()' to iterate through the cursor page by page.
// db.getCollection('sales').aggregate([
//   // Find all of the sales that occurred in 2014.
//   { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
//   // Group the total sales for each product.
//   { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price', '$quantity' ] } } } }
// ]);


show dbs; // show databases 
db;  // show  database 

db.getCollectionNames();   // show tables 

db.users.insertOne({
    'name': ' raj',
    'age' : 20
})                  // to add or to create table 


db.users.insertMany([
    {
        'name':'amit' , 'Branch': 'Comps'
    },
    {
        'name':'Pooja' , 'Job': 'Faculty'
    },
    {
        'name':'Chetana' , 'School': 'LTCE'
    }
])


db.users.find();    //select command            // returns the array of json objects 

db.users.findOne();                     // gives the first record 



use('mydb');       // new database empty
db;
db.users.insertOne({
    'name': ' raj',
    'age' : 20
})                  // to add or to create table 

use('mydb');  
db.users.insertMany([
    {
        'name':'Ketan' , 'Qual': 'Bcom'
    },
    {
        'name':'Rajesh' , 'University': 'Mumbai'
    },
    {
        'name':'Pooja' , 'Job': 'Faculty'
    },
    {
        'name':'Raj' , 'Hobby': 'painting'
    },
    {
        'name':'sagar' , 'Job': 'manager','age':24
    },
    {
        'name':'Ketan' , 'Job': 'Faculty','age':32
    }
])
db.users.find(); 


use ('mydb');
db.users.find({
    name:'Ketan'        // case sensitive
})

use ('mydb');
db.users.find({
    '_id':ObjectId('66ee590792d1daca2573dc7f')
});

use ('mydb');

db.products.insertMany([
    {item: 'pen', price: 20, quantity: 2, colors: ['red', 'blue'], size: {w: 1, h: 10, unit: 'cm' } }, 
    {item: 'pencil', price: 10, quantity: 1, colors: ['red', 'blue', 'green'], size: {w: 2, h: 10, unit: 1}},
    {item: 'book', price: 5, quantity: 10, colors: ['blue', 'red'], size: {w: 10, h: 20, unit: 'cm' } }, 
    {item: 'iphone', price: 50000, quantity: 20, colors: ['grey', 'metal'], size: {w: 5, h: 10, unit: "in"}} ,
    {item: 'tv', price: 10000, quantity: 10, colors: ['red', 'black'], size: { w: 21, h: 17, unit: 'in' }},
    {item: 'sketchpen',price:1000,quantity: 20}
]);
db.products.find();

use ('mydb');
db.products.find({
    price:10
});

use ('mydb');
db.products.find(
    {
        size: { w: 21, h: 17, unit: 'in' }
    }
);

use ('mydb');
db.products.find({
    price:{$gt:10}
});

use ('mydb');
db.products.find({
    item:/pen/          //pattern matching items with pen 
});


use ('mydb');
db.products.find({
    item:/^pen/          //pattern matching  starting items with pen 
});


use('mydb');
db.products.find({
    item:/pen$/          //pattern matching  ending items with pen 
});


use('mydb');
db.products.find({
    item:'pen',        //pattern matching  ending items with pen 
    quantity:2
});

use('mydb');
db.products.find({
    item:/n/,
    quantity:{$gt:1}
})

use('mydb');
db.products.find({
   $or:[{item:/n/},{quantity:2}]
})

use('mydb');
db.products.find({
   $or:[{item:/pen/,price:{$gt:10}},{
    quantity:{$lt:10}}]
})


use('mydb');
db.products.insertMany([
    {item:'pen',quantity: 2, price:20, colors:['red','blue'],size:{w:1,h:10, unit:'cm'}},
    {item:'pencil',quantity: 1, price:10, colors:['red','blue','green'],size:{w:1,h:10, unit:'cm'}},
    {item:'book',quantity: 10, price:45, colors:['red'],size:{w:1,h:20, unit:'cm'}},
    {item:'phone',quantity: 5, price:20000, colors:['red','black'],size:{w:21,h:17, unit:'in'}},
    {item:'sketchpen',quantity: 20, price:15, colors:['red','blue','yellow'],size:{w:1,h:10, unit:'cm'}},

])
use('mydb');
db.products.find({
    size:{w:1,h:20, unit:'cm'}

});
use ('mydb')
db;

use('mydb');
db.products.find({
    'size.h': 17
});

use('mydb');
db.products.find({
    'size.h': {$gte : 10 }
});

use('mydb');
db.products.find({
    'colors.0':'red'
});
use('mydb');
db.products.find({
    colors:{$size: 3}
});
use('mydb');
db.products.find({
    colors:{$eq: 'red'}
});

//delete
//delete the single record where price is greater than 10

use('mydb');
db.products.deleteOne({
    price: {$gt :10}
});



use('mydb');
db.products.deleteMany({
    item: 'pencil'
});

//update
//update the quantity of phone as 50
use('mydb');
db.products.updateOne({
    item: 'phone'},
    {$set: {quantity: 50, price: 150000}}
);
db.products.find();

//Projections

use('mydb');
db.products.find(
    {}, // filterion 
    {
        item:1,
        price:1
    } // projections 
);
use('mydb');
db.products.find().sort(
    {price:1,item:-1}
);

use('mydb');
db.products.find().limit(2); //db count dega

db.products.find().skip(2).limit(2); //2 skip karega baki do dega

use('mydb');
db.orders.insertMany([
    {item:'pen',size:'small',price:10 , quantity:20},
    {item:'pen',size:'medium',price:15 , quantity:10},
    {item:'pencil',size:'small',price:5 , quantity:15},
    {item:'pen',size:'small',price:10 , quantity:5}
]);