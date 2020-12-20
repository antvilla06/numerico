model = createpde();
>> geometryFromEdges(model,@circleg);
>> figure
>> pdegplot(model, 'EdgeLabels', 'on');
>> axis equal
