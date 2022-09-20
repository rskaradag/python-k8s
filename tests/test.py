from node import node

def test_new_node():

	node = Node('node61.app.internal.com')
	node.record_group('group10')
	assert user.email == 'node61.app.internal.com'
	assert node.groups == ['group10']

def test_remove_group():

    node = Node('node61.app.internal.com')
    node.record_group('group10')
    assert user.email == 'node61.app.internal.com'
    assert node.groups == ['group10']