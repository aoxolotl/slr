# Unsupervised techniques for sign language processing 

## Abstract
Despite the progress in natural language processing of spoken languages, deep
learning research for sign languages is still in a very nascent stage. 
However, sign languages are similar to spoken languages in the nature of their 
compositionality and complexity despite a difference in their modality. With
very limited availabilty of sign language transcriptions, it becomes important
to explore unsupervised and weakly supervised techniques that are not reliant on
annotated data. Zero-resource language research for segmentation and term
discovery in speech has recently started gaining traction and we hope to employ 
similar methods and analyze their efficacy for sign languages. More importantly
by treating sign languages no different from speech, we hope to establish ready
transferability of research from spoken languages.

## Related work
Most prior work in sign langauge translation has used techniques to convert
video streams to spoken language transcriptions [1].
This task is hard considering that sign languages have their own syntax and
grammar distinct from the spoken language transcriptions. The task of direct
translation from a sign language to such a transcription would be akin to
directly translating spoken Chinese to English without any intermediate
representation. [Camgoz et. al.][1] improve on the perfomance on the RWTH
Dataset by using glosses to represent sign language utterances before
translating into German. An initial step involves aligning the sign language 
utterances to their glosses. However, transcribing such glosses is a laborious process 
requiring expert annotators. Considering that glosses or similar representations 
for sign languages are not readily available, translation then becomes a zero-resource
task for most sign languages. It is important, as is with other zero resource
languages, to first look at unsupervised techniques in segmentation and term
discovery before we embark on significantly harder tasks such as translation of
sign languages.

Since sign language utterances, like their spoken counterparts, are continuous
in nature, we explore techniques in segmentation, term discovery and embedding
in speech and measure how effective they are in the visual modality. MFCCs are
almost universally used as feature descriptors of speech but sign languages lack
an equivalent descriptor. For the purpose of this research we will limit
ourselves to two approaches for representing sign langauge video frames, namely 
autoencoders and using an intermediate layer of a model pretrained on ImageNet.

## Research Design and Methods
We will be conducting our research on the RWTH Phoenix dataset [5] which contains
over 8 hours of video where the signers are facing the camera. As this dataset
already contains the glosses for the video segments this will allow us to
measure the efficacy of our unsupervised techniques.
1. **Universal term discovery and segmentation:**  
We mainly aim to use Kamper's research [3] for unlabelled speech datasets to segment 
utterances and then cluster them using K-means method. We plan to use set the value of K to
vocabulary of the glosses which implies some amount of supervision. However
the value of K can also easily be approximated by using bilingual dictionaries of word
segments available online.[5]
2. **Sign2Vec:**  
Using the segments obtained from the previous step, we want to employ
another unsupervised approach to generate embeddings in sign languages. Inspired
by Chung et. al [4], we aim to define an end to end unsupervised pipeline from video
streams to sign embeddings and use these embeddings for supervised tasks such as
translation. Like Speech2Vec, we hope to capture greater semantic information in
the Sign2Vec embeddings than the glosses.

## Performance and analysis
Using the glosses from RWTH dataset, we will measure the similarity of the
clusters formed from these glosses and the video streams. Averaging the members
of the clusters, we generate embeddings which are used for downstream tasks such
as translation. We aim to compare the performance of translation task using
these embeddings as a starting point versus an end to end approach such as
[1] without introducing too many changes in the architecture.

## References
[1]: Cihan Camgoz, Necati, et al. "Neural sign language translation." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2018.  
[2]: W. C. Stokoe.  Sign Language Structure.Annual Review ofAnthropology, 9(1), 1980.  
[3]: Kamper, Herman, Karen Livescu, and Sharon Goldwater. "An embedded segmental k-means model for unsupervised segmentation and clustering of speech." 2017 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU). IEEE, 2017.  
[4]: Chung, Yu-An, et al. "Unsupervised cross-modal alignment of speech and text embedding spaces." Advances in Neural Information Processing Systems 2018.  
[5]: https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/  
[6]: https://www.spreadthesign.com
