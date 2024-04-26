function init(){
    //create frames
    const centerer = document.createElement("div");
    centerer.style.width = "80%";
    centerer.style.height = "80%";
    centerer.style.left = "50%";
    centerer.style.top = "45%"; 
    centerer.style.position = "absolute";
    centerer.style.transform = "translate(-50%,-50%)";
    centerer.style.borderRadius = AccessCSSVar("--CornerRad");
    centerer.style.backgroundColor = AccessCSSVar("--col_bg_lighter");
    document.getElementById("content-fullscreen").appendChild(centerer); 

    //const file = new File([myexistingimagefile], './20240412_153915.jpg');
    const file = new File(['./20240412_153915.jpg'], './20240412_153915.jpg');
    file.arrayBuffer().then((buffer) => {
        const reader = new FileReader();
        reader.onload = () => {
            // Do something with the base64-encoded image data.
            const imageData = reader.result;
            console.log(imageData); 
            // Rest of your code here...
        };
        reader.readAsDataURL(buffer);
    });
}



function dqt(bitmap, qr, qg, qb) {
    const height = bitmap.length;
    const width = bitmap[0].length;
    const channels = 3; // RGB
  
    const dctR = new Array(height);
    const dctG = new Array(height);
    const dctB = new Array(height);
  
    for (let i = 0; i < height; i++) {
      dctR[i] = new Array(width);
      dctG[i] = new Array(width);
      dctB[i] = new Array(width);
    }
  
    // Apply DCT to each color channel
    for (let k = 0; k < width; k++) {
      for (let n = 0; n < width; n++) {
        let sumR = 0;
        let sumG = 0;
        let sumB = 0;
  
        for (let m = 0; m < height; m++) {
          sumR += bitmap[m][k] * Math.cos((2 * m + 1) * k / width);
          sumG += bitmap[m][n] * Math.cos((2 * m + 1) * n / width);
          sumB += bitmap[m][n] * Math.cos((2 * m + 1) * n / width);
        }
  
        dctR[i][k] = 2 * sumR;
        dctG[i][n] = 2 * sumG;
        dctB[i][n] = 2 * sumB;
      }
    }
  
    // Quantize each color channel
    const quantizedR = new Array(height);
    const quantizedG = new Array(height);
    const quantizedB = new Array(height);
  
    for (let i = 0; i < height; i++) {
      for (let j = 0; j < width; j++) {
        quantizedR[i][j] = Math.round(dctR[i][j] / qr);
        quantizedG[i][j] = Math.round(dctG[i][j] / qg);
        quantizedB[i][j] = Math.round(dctB[i][j] / qb);
      }
    }
  
    // Return the quantized image and a visualization of frequency
    return [
      // Quantized image
      quantizedR,
      quantizedG,
      quantizedB,
  
      // Frequency visualization (0-255)
      new Array(height).fill(0).map(() => new Array(width).fill(0)),
    ];
}


function getRgbValuesFromJpeg(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        const imgData = reader.result;
        const img = new Image();
        img.src = 'data:image/jpeg;base64,' + imgData;
  
        img.onload = () => {
          const rgbValues = [];
          for (let y = 0; y < img.height; y++) {
            for (let x = 0; x < img.width; x++) {
              const pixel = img.getImageData(x, y).data;
              rgbValues[y] = rgbValues[y] || [];
              rgbValues[y][x] = [pixel[0], pixel[1], pixel[2]];
            }
          }
          resolve(rgbValues);
        };
        img.onerror = () => reject(new Error('Error loading image'));
      };
      reader.readAsDataURL(file);
    });
}