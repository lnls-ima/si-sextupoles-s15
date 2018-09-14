function idcs = permute_randomly(idcs, params)
    n = length(params.data.names);
    id = randperm(n, n);
    idcs = idcs(id);
end