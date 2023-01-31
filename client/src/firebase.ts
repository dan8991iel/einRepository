// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getStorage } from 'firebase/storage';

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAdPt7ejXnHwZSppM6IgTzo4bGm465_sN4",
  authDomain: "sieben-zwerge-webshop.firebaseapp.com",
  projectId: "sieben-zwerge-webshop",
  storageBucket: "sieben-zwerge-webshop.appspot.com",
  messagingSenderId: "621689690374",
  appId: "1:621689690374:web:c37bf0aeb5f6ac35e22687"
};

// Initialize Firebase
export const firebaseApp = initializeApp(firebaseConfig);

export const firebaseStorage = getStorage(firebaseApp);