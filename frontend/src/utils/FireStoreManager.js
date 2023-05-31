import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  getDoc,
  doc,
  getDocs,
} from "firebase/firestore";
import { getFirebaseConfig } from "../firebase-config";

export default function FireStoreManager() {
  const app = initializeApp(getFirebaseConfig());
  const db = getFirestore(app);
  const statsCollectionRef = collection(db, "statistics"); // statistics collection
  console.log("Initialized firestore app");

  async function getSize() {
    const data = await getDocData("database-size");
    if (data) {
      return data.size;
    }
  }

  async function getDocData(docID) {
    console.log(`Requested data for ${docID}`);
    const docRef = doc(statsCollectionRef, docID);
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      console.log("Found data!");
      return docSnap.data();
    }
    console.log("Document does not exist");
    return null;
  }

  async function getAllDocs() {
    const querySnapshot = await getDocs(statsCollectionRef);
    const allData = {};
    querySnapshot.forEach((doc) => {
      // doc.data() is never undefined for query doc snapshots
      allData[doc.id] = doc.data();
      //   allData.push({ id: doc.id, data: doc.data() });
    });
    return allData;
  }

  return {
    getAllDocs,
    getSize,
  };
}
