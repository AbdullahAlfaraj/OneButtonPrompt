import modules.scripts as scripts
import os
from modules import modelloader, paths, shared, sd_models
from modules.paths import models_path


def get_models():
    modellist = sd_models.checkpoint_tiles()
    return modellist

def get_upscalers():
    # Upscalers are sort of hardcoded as well for Latent, but not for the 2 others. So build it up!
    latentlist=["Latent","Latent (antialiased)","Latent (bicubic)","Latent (bicubic antialiased)","Latent (nearest)","Latent (nearest-exact)","Lanczos","Nearest"]

    upscalerlistfromwWebUI = [x.name for x in shared.sd_upscalers]

    upscalerlist = latentlist + upscalerlistfromwWebUI
    return upscalerlist

def get_samplers():
    #Samplers are hardcoded in WEBui, so lets do it here as well
    samplerlist = ["Euler a", "Euler", "LMS","Heun","DPM2","DPM2 a","DPM++ 2S a","DPM++ 2M","DPM++ SDE","DPM fast","DPM adaptive","LMS Karras","DPM2 Karras","DPM2 a Karras","DPM++ 2S a Karras","DPM++ 2M Karras","DPM++ SDE Karras"]
    samplerlist += ["DDIM","UniPC", "PLMS"]
    return samplerlist

def get_upscalers_for_img2img():
    upscalerlistfromwWebUI = [x.name for x in shared.sd_upscalers]
    if("None" in upscalerlistfromwWebUI):
        upscalerlistfromwWebUI.remove("None")
    return upscalerlistfromwWebUI

def get_samplers_for_img2img():
    #Samplers are hardcoded in WEBui, so lets do it here as well
    samplerlist = ["Euler a", "Euler", "LMS","Heun","DPM2","DPM2 a","DPM++ 2S a","DPM++ 2M","DPM++ SDE","DPM fast","DPM adaptive","LMS Karras","DPM2 Karras","DPM2 a Karras","DPM++ 2S a Karras","DPM++ 2M Karras","DPM++ SDE Karras"]
    samplerlist += ["DDIM"] #UniPC and PLMS dont support upscaling apparently
    return samplerlist
