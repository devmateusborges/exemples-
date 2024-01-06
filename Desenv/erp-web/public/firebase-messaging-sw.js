/* eslint-disable no-restricted-globals */
/* eslint-disable prettier/prettier */
/* eslint-disable no-undef */
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

const firebaseConfig = {
    apiKey: "AIzaSyCHXqDSX8Bmnc3lLhV6lwqPAKf65nq5CIA",
    authDomain: "resultfacil-eaa12.firebaseapp.com",
    databaseURL: "https://resultfacil-eaa12.firebaseio.com",
    projectId: "resultfacil-eaa12",
    storageBucket: "resultfacil-eaa12.appspot.com",
    messagingSenderId: "556702444999",
    appId: "1:556702444999:web:9815dde60d6deff567fde2",
};

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log("SW Received background message: ", payload);

    const notificationTitle = payload.notification.title;
    const notificationOptions = { body: payload.notification.body };

    self.registration.showNotification(notificationTitle, notificationOptions);
});
