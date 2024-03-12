<?php
$COUCH_IP = "192.168.50.162";
$COUCH_PORT = "5984";
$COUCH_USER = "admin";
$COUCH_PASS = "lin2017";

class CouchDB {
    private $host;
    private $database = 'protosparky-backend';
    private $cookie = "none";
    private $username;
    private $password;
    private $cookieAuth = false;
    public function __construct() {
        global $COUCH_IP, $COUCH_PORT, $COUCH_USER, $COUCH_PASS;
        $this->host = $COUCH_IP . ':' . $COUCH_PORT;
        $this->username = $COUCH_USER;
        $this->password = $COUCH_PASS;
    }

    // Function to create a new document
    public function createDocument($document) {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $this->host . '/' . $this->database);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($document));
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

        // Add authentication
        if ($this->cookieAuth) {
            curl_setopt($ch, CURLOPT_COOKIE, "AuthSession=".$cookie);
        } else {
            curl_setopt($ch, CURLOPT_USERPWD, $this->username . ':' . $this->password);
        }

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode($response, true);
    }

    // Function to delete a document
    public function deleteDocument($id, $rev) {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $this->host . '/' . $this->database . '/' . $id . '?rev=' . $rev);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode($response, true);
    }

    // Function to get a document
    public function getDocument($id) {
        $ch = curl_init();
    
        curl_setopt($ch, CURLOPT_URL, $this->host . '/' . $this->database . '/' . $id);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
        // Add authentication
        if ($this->cookieAuth) {
            curl_setopt($ch, CURLOPT_COOKIE, "AuthSession=".$cookie);
        } else {
            curl_setopt($ch, CURLOPT_USERPWD, $this->username . ':' . $this->password);
        }
    
        $response = curl_exec($ch);
        curl_close($ch);
    
        return json_decode($response, true);
    }

    // Function to update a document
    public function updateDocument($id, $document) {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $this->host . '/' . $this->database . '/' . $id);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($document));
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
        // Add authentication
        if ($this->cookieAuth) {
            curl_setopt($ch, CURLOPT_COOKIE, "AuthSession=".$cookie);
        } else {
            curl_setopt($ch, CURLOPT_USERPWD, $this->username . ':' . $this->password);
        }
            

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode($response, true);
    }
}


/*

$couchDB = new CouchDB();
// Create a new document
$document = array(
    "_id"=>"users",

);
$response = $couchDB->createDocument($document);
print_r($response);


/*


// Create a new document
$document = array(
    'name' => 'Sparky',
    'type' => 'protogen'
);
$response = $couchDB->createDocument($document);
print_r($response);


*/
// Get a document
$couchDB = new CouchDB();
$documentId = 'UWU';
$response = $couchDB->getDocument($documentId);
print_r($response);

/*
// Update a document
$couchDB = new CouchDB();
$documentId = 'UWU';
$document = array(
    'name' => 'Sparky',
    'type' => 'protogen',
    '_rev' => '2-1a4ec852ae6e8c4a674f2adaf6ee6d93'
);
$response = $couchDB->updateDocument($documentId, $document);
print_r($response);
/*
// Delete a document
$documentId = 'your_document_id';
$rev = 'your_document_revision';
$response = $couchDB->deleteDocument($documentId, $rev);
print_r($response);
*/



?>