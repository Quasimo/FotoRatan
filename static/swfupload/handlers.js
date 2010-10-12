function fileQueueError(file, errorCode, message) {
	
}

function fileQueued(file){
	var progress=new FileProgress(file);
}

function fileDialogComplete(numFilesSelected, numFilesQueued) {
	try {
		if (numFilesQueued > 0) {
			document.getElementById("showResult").innerHTML=numFilesQueued+" Images Selected ";
			this.startUpload();
		}
	} catch (ex) {
		this.debug(ex);
	}
}

function uploadProgress(file, bytesLoaded) {

	try {
		var progress = new FileProgress(file);
		progress.setStatus("Uploading...");
	} catch (ex) {
		this.debug(ex);
	}
}

function uploadSuccess(file, serverData) {
	try {
		var progress = new FileProgress(file);
		var obj = eval('(' + serverData + ')');  
		progress.setStatus(obj.result); 
		if (obj.id>0) {
		addImg(obj.id);
		}
	} catch (ex) {
		this.debug(ex);
	}
}


function uploadComplete(file) {
	try {
		/*  I want the next upload to continue automatically so I'll call startUpload here */
		if (this.getStats().files_queued > 0) {
			this.startUpload();
		} else {
			document.getElementById("showResult").innerHTML="All images Uploaded";
		}
	} catch (ex) {
		this.debug(ex);
	}
}

function uploadError(file, errorCode, message) {
	var progress;
	try {
		var progress = new FileProgress(file);
		progress.setStatus("Error")
	} catch (ex3) {
		this.debug(ex3);
	}

}

function addImg(id){
	var at="/show/{0}/";
	var st="/s/{0}/";
	var target=document.getElementById("imglist");
	
	var imgLiElement=document.createElement("li");

	var imgAElement=document.createElement("a");
	imgAElement.href=at.replace("{0}",id);
	imgAElement.target="_blank";
	
	var imgElement=document.createElement("img");
	imgElement.src=st.replace("{0}",id);
	
	imgAElement.appendChild(imgElement);
	imgLiElement.appendChild(imgAElement);
	
	target.appendChild(imgLiElement);
}
/* ******************************************
 *	FileProgress Object
 *	Control object for displaying file info
 * ****************************************** */

function FileProgress(file){
	this.fileProgressID=file.id;
	this.fatherID=document.getElementById("cFileList");
	this.fileWrapper=document.getElementById(this.fileProgressID);
	if(!this.fileWrapper){
		this.fileWrapper=document.createElement("li");
		this.fileWrapper.id=this.fileProgressID;
		
		var sFileName=document.createElement("span");
		sFileName.className="filename";
		sFileName.innerHTML=file.name;
		
		var sFileState=document.createElement("span");
		sFileState.className="filestate";
		sFileState.innerHTML="Lock";
		
		this.fileWrapper.appendChild(sFileName);
		this.fileWrapper.appendChild(sFileState);
		
		this.fatherID.appendChild(this.fileWrapper);
	}
	
	FileProgress.prototype.setStatus=function (status){
		this.fileWrapper.childNodes[1].innerHTML=status;
	}
}