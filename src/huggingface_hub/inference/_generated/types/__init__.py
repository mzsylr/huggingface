# This file is auto-generated by `utils/generate_inference_types.py`.
# Do not modify it manually.
#
# ruff: noqa: F401

from .audio_classification import (
    AudioClassificationInput,
    AudioClassificationOutputElement,
    AudioClassificationParameters,
)
from .audio_to_audio import AudioToAudioInput, AudioToAudioOutputElement
from .automatic_speech_recognition import (
    AutomaticSpeechRecognitionGenerationParameters,
    AutomaticSpeechRecognitionInput,
    AutomaticSpeechRecognitionOutput,
    AutomaticSpeechRecognitionOutputChunk,
    AutomaticSpeechRecognitionParameters,
)
from .base import BaseInferenceType
from .chat_completion import (
    ChatCompletionInput,
    ChatCompletionInputMessage,
    ChatCompletionOutput,
    ChatCompletionOutputChoice,
    ChatCompletionOutputChoiceMessage,
    ChatCompletionStreamOutput,
    ChatCompletionStreamOutputChoice,
    ChatCompletionStreamOutputDelta,
)
from .depth_estimation import DepthEstimationInput, DepthEstimationOutput
from .document_question_answering import (
    DocumentQuestionAnsweringInput,
    DocumentQuestionAnsweringInputData,
    DocumentQuestionAnsweringOutputElement,
    DocumentQuestionAnsweringParameters,
)
from .feature_extraction import FeatureExtractionInput
from .fill_mask import FillMaskInput, FillMaskOutputElement, FillMaskParameters
from .image_classification import (
    ImageClassificationInput,
    ImageClassificationOutputElement,
    ImageClassificationParameters,
)
from .image_segmentation import ImageSegmentationInput, ImageSegmentationOutputElement, ImageSegmentationParameters
from .image_to_image import ImageToImageInput, ImageToImageOutput, ImageToImageParameters, ImageToImageTargetSize
from .image_to_text import ImageToTextGenerationParameters, ImageToTextInput, ImageToTextOutput, ImageToTextParameters
from .object_detection import (
    ObjectDetectionBoundingBox,
    ObjectDetectionInput,
    ObjectDetectionOutputElement,
    ObjectDetectionParameters,
)
from .question_answering import (
    QuestionAnsweringInput,
    QuestionAnsweringInputData,
    QuestionAnsweringOutputElement,
    QuestionAnsweringParameters,
)
from .sentence_similarity import SentenceSimilarityInput, SentenceSimilarityInputData
from .summarization import SummarizationGenerationParameters, SummarizationInput, SummarizationOutput
from .table_question_answering import (
    TableQuestionAnsweringInput,
    TableQuestionAnsweringInputData,
    TableQuestionAnsweringOutputElement,
)
from .text2text_generation import Text2TextGenerationInput, Text2TextGenerationOutput, Text2TextGenerationParameters
from .text_classification import TextClassificationInput, TextClassificationOutputElement, TextClassificationParameters
from .text_generation import (
    TextGenerationInput,
    TextGenerationOutput,
    TextGenerationOutputDetails,
    TextGenerationOutputSequenceDetails,
    TextGenerationOutputToken,
    TextGenerationParameters,
    TextGenerationPrefillToken,
    TextGenerationStreamDetails,
    TextGenerationStreamOutput,
)
from .text_to_audio import TextToAudioGenerationParameters, TextToAudioInput, TextToAudioOutput, TextToAudioParameters
from .text_to_image import TextToImageInput, TextToImageOutput, TextToImageParameters, TextToImageTargetSize
from .token_classification import (
    TokenClassificationInput,
    TokenClassificationOutputElement,
    TokenClassificationParameters,
)
from .translation import TranslationGenerationParameters, TranslationInput, TranslationOutput
from .video_classification import (
    VideoClassificationInput,
    VideoClassificationOutputElement,
    VideoClassificationParameters,
)
from .visual_question_answering import (
    VisualQuestionAnsweringInput,
    VisualQuestionAnsweringInputData,
    VisualQuestionAnsweringOutputElement,
    VisualQuestionAnsweringParameters,
)
from .zero_shot_classification import (
    ZeroShotClassificationInput,
    ZeroShotClassificationInputData,
    ZeroShotClassificationOutputElement,
    ZeroShotClassificationParameters,
)
from .zero_shot_image_classification import (
    ZeroShotImageClassificationInput,
    ZeroShotImageClassificationInputData,
    ZeroShotImageClassificationOutputElement,
    ZeroShotImageClassificationParameters,
)
from .zero_shot_object_detection import (
    ZeroShotObjectDetectionBoundingBox,
    ZeroShotObjectDetectionInput,
    ZeroShotObjectDetectionInputData,
    ZeroShotObjectDetectionOutputElement,
)
