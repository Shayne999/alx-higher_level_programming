#!/usr/bin/node

//computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode === 200) {
        const completed = {};
        const tasks = JSON.parse(body);

        for (const task of tasks) {
            if (task.completed) {
                if (!completed[task.userId]) {
                    completed[task.userId] = 1;
                } else {
                    completed[task.userId]++;
                }
            }
        }

        console.log(completed);
    } else {
        console.error('An error occurred. Status code:', response.statusCode);
    }
});

