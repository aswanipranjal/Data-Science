function demo_eigshow()
    // create the plot
    A = [1 2;3 4];
    hmatrix = scf()
    // scidemo_matrixeigshow(A)

    gwidth = 200;
    gheight = 250;
    cwidth = round(0.9*gwidth);
    cheight = 20;

    hmain = scf();
    drawlater()
    matrixdb = [
        '[1 2;3 4]'
        '[1 2;-6 4]'
        '[1 0;0 2]'
        '[1 1;1 1]'
        '[0 0;0 0]'
        '[-1 0;0 1]'
        '[-1 0;0 -1]'
    ];
    hfig = figure(hmain);
    hfig.axes_size = [gwidth gheight];

    // A slider for the base matrix
    y = hfig.axes_size(2) - 120;
    huilist = uicontrol(hfig, 'style', 'listbox');
    huilist.Position = [10 y cwidth 120];
    huilist.String = matrixdb;
    huilist.Value = 1;
    huilist.BackgroundColor = [1 1 1];
    huilist.Callback = 'demo_eigshowcallback';

    // A text for the symmetry
    y = y - cheight;
    huisymtext = uicontrol(hfig, 'style', 'text');
    huisymtext.Position = [10 y cwidth cheight];
    huisymtext.String = 'Symmetry:0';
    huisymtext.BackgroundColor = [1 1 1];

    // A slider for the symmetry
    y = y - cheight;
    huisym = uicontrol(hfig, 'style', 'slider');
    huisym.Position = [10 y cwidth cheight];
    huisym.Min = 0;
    huisym.Max = 256;
    huisym.Value = 0;
    huisym.Callback = 'demo_eigshowcallback';

    // A text for the matrix
    y = y - cheight;
    huimattext = uicontrol(hfig, 'style', 'text');
    huimattext.Position = [10 y cwidth cheight];
    huimattext.String = 'Matrix=';
    huimattext.BackgroundColor = [1 1 1];

    drawnow()

    global eigshowgui;
    eigshowgui = tlist(['EIGSHOHUI', 'hmatrix', 'hmain', 'hfig', 'huilist', 'matrixdb', 'huisym', 'huisymtext', 'huimattext'])
    eigshowgui.hmain = hmain;
    eigshowgui.hfig = hfig;
    eigshowgui.huilist = huilist;
    eigshowgui.matrixdb = matrixdb;
    eigshowgui.hmatrix = hmatrix;
    eigshowgui.huisym = huisym;
    eigshowgui.huisymtext = huisymtext;
    eigshowgui.huimattext = huimattext;

    demo_eigshowcallback()
endfunction

function demo_eigshowcallback()
    execstr('demo_eigshowcallback_do', 'errcatch')
endfunction

function demo_eigshowcallback_do()
    global eigshowgui;
    hmain = eigshowgui.hmain;
    hfig = eigshowgui.hfig;
    huilist = eigshowgui.huilist;
    matrixdb = eigshowgui.matrixdb;
    hmatrix = eigshowgui.hmatrix;
    huisym = eigshowgui.huisym;
    huisymtext = eigshowgui.huisymtext;
    huimattext = eigshowgui.huimattext;
    // Get the user's choice
    demochoice = huilist.Value;

    drawlater()
    // clf(hmatrix)
    scf(hmatrix);
    instr = 'A='+matrixdb(demochoice);
    execstr(instr)
    t = (huisym.Value)/256
    huisymtext.String = 'Symmetry:' + string(t);
    B = t * (A + A')/2 + (1 - t) * A;
    huimattext.String = 'Matrix=' + msprintf('[%.3f %.3f; %.3f %.3f]', B(1, 1), B(1, 2), B(2, 1), B(2, 2));
    scidemo_matrixeigshowupd(hmatrix, B)
    drawnow()
endfunction

function scidemo_matrixeigshowupd(hmatrix, A)

    // update only the minimum amount of data, to improve speed
    [R, D] = spec(A);
    if (isreal(D(1, 1))) then
        d1 = msprintf('%.3f', D(1, 1))
    else
        d1 = msprintf('%.3f + i*%.3f', real(D(1, 1)), imag(D(1, 1)))
    end

    if (isreal(D(2, 2))) then
        d2 = msprintf('%.3f', D(2, 2))
    else
        d2 = msprintf('%.3f + i*%.3f', real(D(2, 2)), imag(D(2, 2)))
    end
    thetitle = 'Eigenvalues: l1=' + d1 + ', l2=' + d2
    hmatrix.children.title.text = thetitle

    // update the ellipse
    t = linspace(0, 2*%pi, 1000);
    x = [cos(t); sin(t)];
    b = A * x;
    hmatrix.children(1).children(3).children.data = [b(1,:)' b(2,:)']

    // update the eigenvectors
    hmatrix.children(1).children(1).children.data(2,:) = R(:,1)'
    hmatrix.children(1).children(2).children.data(2,:) = R(:,2)'
    
    // update the bounds
    m = max([max(abs(b)) 1])
    hmatrix.children.data_bounds = [-m -m;m m];
endfunction

demo_eigshow();
clear demo_eigshow;
