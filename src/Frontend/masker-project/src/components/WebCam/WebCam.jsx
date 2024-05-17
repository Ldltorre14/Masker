import React, {useRef, useEffect, useState} from "react";
import "./WebCam.css"


function WebCam(){
    const videoRef = useRef(null)
    const photoRef = useRef(null)

    const [hasPhoto, setHasPhoto] = useState(false)

    const getVideo = () => {
        navigator.mediaDevices.getUserMedia({video : {
            width: 1920, height: 1080}
        })
        .then(stream => {
            let video = videoRef.current
            video.srcObject = stream
            video.play()
        })
        .catch(err => {
            console.error(err)
        })
    }

    useEffect(() => {
        getVideo()
    },[videoRef])

    return (
        <div className="camera">
            <video ref={videoRef}></video>
        </div>

    )

}

export default WebCam