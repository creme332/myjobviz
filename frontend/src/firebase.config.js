/**
 * To find your Firebase config object:
 *
 * 1. Go to your [Project settings in the Firebase console](https://console.firebase.google.com/project/_/settings/general/)
 * 2. In the "Your apps" card, select the nickname of the app for which you need a config object.
 * 3. Select Config from the Firebase SDK snippet pane.
 * 4. Copy the config object snippet, then add it here.
 */
//! Add security rules to your database before exposing config publicly
//! Reference: https://stackoverflow.com/a/37484053/17627866
const config = {
  apiKey: "AIzaSyAG6Z2cMJGVqlZ4ZGXWwBZe5hCaAqdFgD0",
  authDomain: "myjobviz.firebaseapp.com",
  projectId: "myjobviz",
  storageBucket: "myjobviz.appspot.com",
  messagingSenderId: "996110286846",
  appId: "1:996110286846:web:f3d5803863efe22b424aaf",
};

export function getFirebaseConfig() {
  if (!config || !config.apiKey) {
    throw new Error(
      "No Firebase configuration object provided." +
        "\n" +
        "Add your web app's configuration object to firebase-config.js"
    );
  } else {
    return config;
  }
}
