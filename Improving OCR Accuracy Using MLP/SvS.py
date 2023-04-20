list_image_files('F:/OCR PROJECT/Custom Font/Blusheets/Character ROICropped - complte sheet', 'default', [], ImageFiles)
for j:=0 to |ImageFiles|-1 by 1 read_image(Image, ImageFiles[j]) rgb1_to_gray(Image, GrayImage)
ThresholdValue:=0.5
local_threshold(GrayImage, Region, 'adapted_std_deviation', 'dark', ['scale', 'mask_size'],[ThresholdValue,50])
*	local_threshold(GrayImage, Region1, 'adapted_std_deviation', 'dark', [], [])connection(Region, ConnectedRegions)
sort_region(ConnectedRegions, SortedRegions, 'character', 'true', 'row') count_obj(SortedRegions, Number)
stop()k:=3
for i:=1 to |Number| by 1


select_obj(SortedRegions, ObjectSelected, i) region_features(ObjectSelected,'width',Width) region_features(ObjectSelected,'height',Height) smallest_rectangle1(ObjectSelected, Row1, Column1, Row2, Column2) gen_rectangle1(Rectangle, Row1, Column1, Row2, Column2) vector_angle_to_rigid(Row1, Column1, 0, Row2, Column2, 0, HomMat2D) affine_trans_region(Rectangle,RegionAffineTrans, HomMat2D, 'nearest_neighbor')hom_mat2d_identity (HomMat2DIdentity)
hom_mat2d_translate(HomMat2DIdentity, -Row1 , -Column1 , HomMat2DTranslate) affine_trans_region(ObjectSelected,RegionAffineTrans1, HomMat2DTranslate,
'nearest_neighbor')
region_to_bin(RegionAffineTrans1, BinImage, 0, 255, Width, Height) get_domain(BinImage, Domain)

write_image(BinImage, 'bmp', 0, 'C:/Users/SRI/Desktop/OCR/New Characters/S_'+(k)+'.bmp')
*k:=k+1stop() endfor
*stop()Endfor

list_image_files	('C:/Users/Desktop/OCR/New	Bin	Images',	'default',	[], ImageFiles)gen_empty_obj(CharacterImages)
read_ocr_class_mlp ('Document_0-9A-Z_NoRej.omc', OCRHandle1) dev_update_off()
SortedClasses := []
for i:=0 to |ImageFiles|-1 by 1 read_image(Image, ImageFiles[i]) threshold(Image, Region, 0,150)
do_ocr_multi_class_mlp (Region, Image, OCRHandle1, Class, Confidence)
*	do_ocr_single_class_mlp(Region, Image, OCRHandle1, 4, Class1, Confidence1)if(Class='O')
stop() Class:='0' endif if(i==335) Class:='U'endif
SortedClasses:=[SortedClasses,Class] concat_obj(CharacterImages,Image,CharacterImages)
endfor
stop()


count_obj(CharacterImages, Number)CharacterToMatch:=[]


for i:=0 to |ImageFiles|-1 by 1 CharacterToMatch:=SortedClasses[i] read_image(Image1, ImageFiles[i])
ThresholdValue:=0.5
local_threshold(Image1, Region, 'adapted_std_deviation', 'dark', ['scale'], [ThresholdValue])
append_ocr_trainf(Region, Image1,CharacterToMatch, 'C:/Users/SRI/Desktop/OCR/Scripts/spaceless_binImage_font.trf')endfor

stop()
create_ocr_class_mlp(10,13, 'constant', ['gradient_8dir', 'pixel_invar', 'ratio', 'moments_region_2nd_invar'], ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',' R','S','T','
U','V','W','X','Y','Z'], 50, 'principal_components', 61, 42, OCRCustom)
* set_regularization_params_ocr_class_mlp (OCRCustom, 'weight_prior', [0.01,0.01,0.01,0.01])
trainf_ocr_class_mlp(OCRCustom, 'C:/Users/SRI/Desktop/OCR/Scripts/spaceless_binImage_font.trf', 200, 1,
0.000001, Error,ErrorLog) write_ocr_class_mlp(OCRCustom,
'C:/Users/SRI/Desktop/OCR/Scripts/SpacelessBinFont[0-9,A- Z][Features][withREGPARAM].omc')



list_image_files('F:/OCR PROJECT/Custom Font/Blusheets/Character ROI Cropped -complte sheet', 'default', [],ImageFiles)
ThresholdValue:=0.5 read_ocr_class_mlp('Document_0-9A-
Z_NoRej.omc',InbuiltFontHandle) read_ocr_class_mlp('F:/OCR PROJECT/Custom Font/Trf and Omc file/SpacelessBinFont[0-9,A- Z][Features][withREGPARAM].omc', ProposedFontHandle)for i:=0 to
|ImageFiles|-1 by 1
read_image(Image, ImageFiles[i])rgb1_to_gray(Image, GrayImage) local_threshold(GrayImage, Region, 'adapted_std_deviation', 'dark',
['scale', 'mask_size'],[ThresholdValue,50])


connection(Region, ConnectedRegions) sort_region(ConnectedRegions, SortedRegions, 'character', 'true', 'row')
do_ocr_multi_class_mlp(SortedRegions, GrayImage, ProposedFontHandle, SVSClass,SVSConfidence)
do_ocr_multi_class_mlp(SortedRegions, GrayImage, InbuiltFontHandle,InbuiltFontClass, InbuiltFontConfidence)
stop() endfor