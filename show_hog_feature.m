img = single(imread('/Users/jennifer/Box Sync/2014 - 2015/cs 231n/project/code/7.png'));
cellSize =3;
hog = vl_hog(img, cellSize, 'verbose');
imhog = vl_hog('render', hog, 'verbose');
clf ; imagesc(imhog) ; colormap gray ;
axis off;
set(gca,'position',[0 0 1 1],'units','normalized');