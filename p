---
- name: Generate configuration templates
  hosts: localhost
  gather_facts: no
  vars_files:
    - inventory.yaml

  tasks:
    - name: Debug inventory_hosts
      debug:
        var: inventory_hosts

    - name: Create templates for each host
      template:
        src: templates/template.j2
        dest: "configs/{{ item.hostname }}.conf"
      loop: "{{ inventory_hosts }}"
      loop_control:
        label: "{{ item.hostname }}"
