For proper functioning list of technical capabilitiesis needed:

1.  model name

2.  model family

3.  maximum context window (in tokens).

4.  training data cut-off date

5.  image files formats supported

6.  audio file processing

    *   direct?

7.  native video support

    *   native video input (e.g., MP4) or 
    
    *   keyframe analysis?

8. video support temporal type

    *   understanding (action over time) 
    
    *   scene detection only

provide data in structured JSON format:

```json
{
    // or "gpt-4o" for the full‑size variant
    "model": "gpt-4o-mini",
    "model_family": ""          
    "max_input_tokens": 128000,
    "max_output_tokens": 4096,
    "supported_image_formats": 
    [
        "jpeg","png","gif","bmp","webp","tiff"
    ],
    "max_image_size_mb": 5,
    "max_image_pixels": 4096000,
    "max_images_per_request": 10,
    "video_support": "frame‑by‑frame (extract & send as images)",
    "audio_support": "text‑only (transcribe first)",
    "video_support_temporal": "scene detectio onlyn",
}
```